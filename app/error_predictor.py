from sklearn.ensemble import IsolationForest
import numpy as np

class ErrorPatternDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.error_patterns = {
            "mislabel": ["wrong_patient", "wrong_test", "duplicate_order"],
            "preanalytical": ["hemolyzed", "clotted", "insufficient"],
            "analytical": ["qc_failure", "calibration_error", "instrument_error"]
        }
    
    def detect_anomaly(self, test_data):
        """Detect anomalous patterns that might indicate errors"""
        anomaly_score = self.model.decision_function([test_data])[0]
        if anomaly_score < -0.5:
            return {
                "anomaly_detected": True,
                "risk_level": "HIGH",
                "recommended_action": "Manual review required"
            }
        return {"anomaly_detected": False}
    
    def predict_error_risk(self, staff_id, shift, volume, error_history):
        """Predict likelihood of error based on multiple factors"""
        risk_score = 0
        if shift == "second":
            risk_score += 0.3  # Higher risk on 2nd shift
        if volume > 500:
            risk_score += 0.2
        if error_history > 2:
            risk_score += 0.4
        
        return {
            "staff_id": staff_id,
            "risk_score": risk_score,
            "risk_level": "HIGH" if risk_score > 0.6 else "MEDIUM" if risk_score > 0.3 else "LOW"
        }
