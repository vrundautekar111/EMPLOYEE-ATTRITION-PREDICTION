document
    .getElementById("predictionForm")
    .addEventListener("submit", async function(event) {

        event.preventDefault();


        const loading =
            document.getElementById("loading");

        const result =
            document.getElementById("result");


        loading.style.display = "block";

        result.style.display = "none";


        const employeeData = {

            age:
                document.getElementById("age").value,

            monthly_income:
                document.getElementById(
                    "monthly_income"
                ).value,

            job_level:
                document.getElementById(
                    "job_level"
                ).value,

            years_at_company:
                document.getElementById(
                    "years_at_company"
                ).value,

            years_current_role:
                document.getElementById(
                    "years_current_role"
                ).value,

            years_promotion:
                document.getElementById(
                    "years_promotion"
                ).value,

            years_manager:
                document.getElementById(
                    "years_manager"
                ).value,

            job_satisfaction:
                document.getElementById(
                    "job_satisfaction"
                ).value,

            environment_satisfaction:
                document.getElementById(
                    "environment_satisfaction"
                ).value,

            work_life_balance:
                document.getElementById(
                    "work_life_balance"
                ).value,

            overtime:
                document.getElementById(
                    "overtime"
                ).value,

            distance_from_home:
                document.getElementById(
                    "distance_from_home"
                ).value,

            companies_worked:
                document.getElementById(
                    "companies_worked"
                ).value,

            training:
                document.getElementById(
                    "training"
                ).value

        };


        try {

            const response = await fetch(
                "/predict",
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify(employeeData)

                }
            );


            const data =
                await response.json();


            loading.style.display = "none";

            result.style.display = "block";


            if (data.error) {

                document.getElementById(
                    "prediction"
                ).innerText =
                    "Error: " + data.error;

                return;

            }


            document.getElementById(
                "prediction"
            ).innerText =
                data.prediction;


            document.getElementById(
                "risk"
            ).innerText =
                "Risk Level: " + data.risk;


            document.getElementById(
                "probability"
            ).innerText =
                data.probability + "%";


        } catch (error) {

            loading.style.display = "none";

            result.style.display = "block";

            document.getElementById(
                "prediction"
            ).innerText =
                "Unable to connect to server.";

            console.error(error);

        }

    });