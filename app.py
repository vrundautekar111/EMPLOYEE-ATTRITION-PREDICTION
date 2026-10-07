from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd


app = Flask(__name__)


model = joblib.load("attrition_model.pkl")

print("Attrition model loaded successfully!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        age = float(data["age"])
        monthly_income = float(data["monthly_income"])
        job_level = float(data["job_level"])
        years_at_company = float(data["years_at_company"])
        years_current_role = float(data["years_current_role"])
        years_promotion = float(data["years_promotion"])
        years_manager = float(data["years_manager"])
        job_satisfaction = float(data["job_satisfaction"])
        environment_satisfaction = float(
            data["environment_satisfaction"]
        )
        work_life_balance = float(
            data["work_life_balance"]
        )

        overtime = data["overtime"]

        distance_from_home = float(
            data["distance_from_home"]
        )

        companies_worked = float(
            data["companies_worked"]
        )

        training = float(
            data["training"]
        )

        overtime_value = 1 if overtime == "Yes" else 0


        input_data = pd.DataFrame([{

            "Age": age,

            "MonthlyIncome": monthly_income,

            "JobLevel": job_level,

            "YearsAtCompany": years_at_company,

            "YearsInCurrentRole": years_current_role,

            "YearsSinceLastPromotion": years_promotion,

            "YearsWithCurrManager": years_manager,

            "JobSatisfaction": job_satisfaction,

            "EnvironmentSatisfaction": environment_satisfaction,

            "WorkLifeBalance": work_life_balance,

            "OverTime": overtime_value,

            "DistanceFromHome": distance_from_home,

            "NumCompaniesWorked": companies_worked,

            "TrainingTimesLastYear": training

        }])



        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        probability_percentage = round(
            probability * 100,
            2
        )


        if prediction == 1:

            result = "Employee is likely to leave"

            risk = "High Risk"

        else:

            result = "Employee is likely to stay"

            risk = "Low Risk"


        return jsonify({

            "prediction": result,

            "risk": risk,

            "probability": probability_percentage

        })


    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 400


if __name__ == "__main__":

    app.run(
        debug=True,
        port=8080
    )