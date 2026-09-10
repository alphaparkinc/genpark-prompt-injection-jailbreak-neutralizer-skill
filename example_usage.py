from client import PromptInjectionJailbreakNeutralizerClient

def main():
    client = PromptInjectionJailbreakNeutralizerClient()
    res = client.neutralize_prompt_injection()
    print('Prompt Injection Neutralizer: ' + res['neutralization_id'] + ' (' + res['risk_severity_grade'] + ')')
    print('Detected: ' + str(res['adversarial_attempt_detected']) + ' | Flags: ' + str(res['flagged_threat_categories']))
    print('Sanitized: ' + res['sanitized_clean_prompt'])
    print('Incident Report: ' + res['security_incident_report_url'])

if __name__ == '__main__':
    main()
