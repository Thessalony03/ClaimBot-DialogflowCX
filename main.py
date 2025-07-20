from flask import jsonify, Request

def app(request: Request):
    req = request.get_json(silent=True)

    session_params = req['sessionInfo']['parameters']

    policy_id = session_params.get('policy_id', 'UNKNOWN')
    date_of_incident = session_params.get('date_of_incident', 'UNKNOWN')
    claim_type = session_params.get('claim_type', 'UNKNOWN')
    claim_amount = session_params.get('claim_amount', 0)

    claim_amount = float(claim_amount)
    fraud_flag = "Suspicious" if claim_amount > 50000 else "Normal"

    if fraud_flag == "Suspicious":
        message = "Your claim looks suspicious. A human agent will assist you shortly."
    else:
        message = f"Your claim has been submitted successfully! Policy ID: {policy_id}, Amount: {claim_amount}"

    response = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [message]
                    }
                }
            ]
        },
        "session_info": {
            "parameters": {
                "fraud_flag": fraud_flag
            }
        }
    }

    return jsonify(response)
