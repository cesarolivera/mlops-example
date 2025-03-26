from flask import Flask, render_template, request, jsonify
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
import pandas as pd
import os
from pathlib import Path

# Initialize Flask App
app = Flask(__name__)

# Bootstrap Kedro project
project_path = Path(__file__).resolve().parent
bootstrap_project(Path.cwd())

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            print("Hello")
            # Get input values from form
            engines                     = float(request.form["engines"])
            passenger_capacity          = int(request.form["passenger_capacity"])
            crew                        = float(request.form["crew"])
            d_check_complete            = "d_check_complete" in request.form
            moon_clearance_complete     = "moon_clearance_complete" in request.form
            iata_approved               = "iata_approved" in request.form
            company_rating              = float(request.form["company_rating"])
            review_scores_rating        = float(request.form["review_scores_rating"])

            # Create input dataframe
            input_data = pd.DataFrame([{
                "engines": engines,
                "passenger_capacity": passenger_capacity,
                "crew": crew,
                "d_check_complete" : d_check_complete,
                "moon_clearance_complete" : moon_clearance_complete,
                "iata_approved" : iata_approved,
                "company_rating" : company_rating,
                "review_scores_rating" : review_scores_rating
            }])

            # Save input data to CSV (for Kedro to read)
            input_data.to_csv("gs://mlops-bucket-gcs/data/05_model_input/input_data.csv", index=False)

            print(input_data)
            # Run Kedro pipeline with input data
            with KedroSession.create() as session:
                result = session.run()
                print(result)
                predicted_price = result["predicted_price"]  # Adjust this based on your Kedro pipeline output
            
            return render_template("index.html", aswer=1, prediction=int(predicted_price))
        except Exception as e:
            return render_template("index.html", error=str(e))
    
    return render_template("index.html", prediction=None, error=None)


@app.route("/run_pipeline")
def run_pipeline():
    with KedroSession.create() as session:
        session.run()  # Runs the default pipeline
    return jsonify({"message": "Pipeline executed successfully!"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080
    app.run(host="0.0.0.0", port=port)