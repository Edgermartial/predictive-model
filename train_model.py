# Load the dataset for training
def load_data():
    try:
        data = pd.read_csv(r"C:\Users\edger\Desktop\AED PROJECT\archive\ai 2020.csv")
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error loading dataset: {e}")
        return None

# Train the Random Forest Classifier and save the model
def train_model():
    data = load_data()
    if data is None:
        return
    
    # Select features and target variable
    X = data[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]',
              'Torque [Nm]', 'Tool wear [min]']]
    y = data['Machine failure']  # Classification target

    # Split the data into training and testing sets (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Classifier Model with adjusted hyperparameters
    rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=10, random_state=42)
    rf_model.fit(X_train, y_train)

    # Save the trained Random Forest model
    joblib.dump(rf_model, 'machine_failure_model.pkl')

    # Evaluate the Random Forest model
    from sklearn.metrics import accuracy_score
    rf_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_pred)  # Accuracy score for classification task
    messagebox.showinfo("Model Training", f"Model Training Complete!\nAccuracy: {rf_accuracy:.2f}")
