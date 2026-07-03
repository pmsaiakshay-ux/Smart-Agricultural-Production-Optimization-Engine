import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend to prevent UI popups during training
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report, confusion_matrix
from preprocess import prepare_data

# Paths
STATIC_IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')

def train_models():
    # Make sure output directories exist
    os.makedirs(STATIC_IMG_DIR, exist_ok=True)
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    # 1. Load preprocessed data
    print("Preparing data...")
    X_train, X_test, y_train, y_test, feature_names, label_encoder = prepare_data()
    
    # 2. Define models
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'KNN': KNeighborsClassifier(n_neighbors=5),
        'SVM': SVC(probability=True, random_state=42),
        'Naive Bayes': GaussianNB()
    }
    
    results = {}
    trained_models = {}
    
    # 3. Train and compare models
    print("\nTraining and evaluating models:")
    print("=" * 60)
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
        
        results[name] = {
            'accuracy': acc,
            'precision': precision,
            'recall': recall,
            'f1': f1
        }
        trained_models[name] = model
        
        print(f"{name:20} -> Accuracy: {acc:.4f} | Precision: {precision:.4f} | Recall: {recall:.4f} | F1: {f1:.4f}")
        
    print("=" * 60)
    
    # 4. Find the best model
    best_model_name = max(results, key=lambda k: results[k]['accuracy'])
    best_model = trained_models[best_model_name]
    best_metrics = results[best_model_name]
    
    print(f"\nBest Model: {best_model_name} with Accuracy: {best_metrics['accuracy']:.4f}")
    
    # Save the best model
    best_model_path = os.path.join(MODEL_DIR, 'model.pkl')
    joblib.dump(best_model, best_model_path)
    print(f"Saved best model to {best_model_path}")
    
    # Write accuracy comparison text file for flask app to read
    results_df = pd.DataFrame(results).T.reset_index().rename(columns={'index': 'Model'})
    results_df.to_csv(os.path.join(MODEL_DIR, 'model_comparison.csv'), index=False)
    
    # 5. Generate and Save Visualizations
    
    # 5.1 Model Accuracy Comparison Graph
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x='accuracy', y='Model', data=results_df, palette='viridis', hue='Model', legend=False)
    plt.xlim(0.8, 1.02)
    plt.title('Machine Learning Models Accuracy Comparison', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Accuracy Score', fontsize=12)
    plt.ylabel('Model Name', fontsize=12)
    
    # Annotate bars
    for p in ax.patches:
        width = p.get_width()
        ax.text(width + 0.005, p.get_y() + p.get_height()/2, f'{width:.4f}', 
                va='center', ha='left', fontsize=10, fontweight='bold')
                
    plt.tight_layout()
    comparison_graph_path = os.path.join(STATIC_IMG_DIR, 'model_comparison.png')
    plt.savefig(comparison_graph_path, dpi=300)
    plt.close()
    print(f"Accuracy comparison graph saved to {comparison_graph_path}")
    
    # 5.2 Feature Importance (if using Random Forest or Decision Tree)
    if hasattr(best_model, 'feature_importances_'):
        importances = best_model.feature_importances_
        feat_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feat_df = feat_df.sort_values(by='Importance', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Importance', y='Feature', data=feat_df, palette='crest', hue='Feature', legend=False)
        plt.title(f'Feature Importance (Best Model: {best_model_name})', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Relative Importance', fontsize=12)
        plt.ylabel('Features', fontsize=12)
        plt.tight_layout()
        
        feat_graph_path = os.path.join(STATIC_IMG_DIR, 'feature_importance.png')
        plt.savefig(feat_graph_path, dpi=300)
        plt.close()
        print(f"Feature importance graph saved to {feat_graph_path}")
    else:
        # If best model doesn't have feature importances (like KNN/SVM/NB), generate it from Random Forest
        rf_model = trained_models['Random Forest']
        importances = rf_model.feature_importances_
        feat_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feat_df = feat_df.sort_values(by='Importance', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Importance', y='Feature', data=feat_df, palette='crest', hue='Feature', legend=False)
        plt.title('Feature Importance (Random Forest Reference)', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Relative Importance', fontsize=12)
        plt.ylabel('Features', fontsize=12)
        plt.tight_layout()
        
        feat_graph_path = os.path.join(STATIC_IMG_DIR, 'feature_importance.png')
        plt.savefig(feat_graph_path, dpi=300)
        plt.close()
        print(f"Feature importance graph saved to {feat_graph_path} (Fallback to Random Forest)")
        
    # 5.3 Confusion Matrix for the Best Model
    y_pred_best = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred_best)
    labels = label_encoder.classes_
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=labels, yticklabels=labels)
    plt.title(f'Confusion Matrix - {best_model_name}', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Predicted Labels', fontsize=12)
    plt.ylabel('True Labels', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    cm_graph_path = os.path.join(STATIC_IMG_DIR, 'confusion_matrix.png')
    plt.savefig(cm_graph_path, dpi=300)
    plt.close()
    print(f"Confusion matrix graph saved to {cm_graph_path}")
    
    # 6. Detail Classification Report
    print("\nDetailed Classification Report for the Best Model:")
    print("=" * 60)
    print(classification_report(y_test, y_pred_best, target_names=labels))
    print("=" * 60)

if __name__ == '__main__':
    train_models()
