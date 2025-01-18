# Custom decorator for logging actions
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"🔍 Logging: {func.__name__} called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ Action logged for: {args[0]['name']}")
        return result
    return wrapper

# Custom decorator for sending notifications
def notify_high_value_lead(func):
    def wrapper(*args, **kwargs):
        lead = args[0]  # The lead being processed
        result = func(*args, **kwargs)
        if lead.get("deal_size", 0) >= 1_000_000:
            print(f"📧 Notification: High-value lead added: {lead['name']} (${lead['deal_size']:,})")
        return result
    return wrapper

# CRM system function to add a lead
@log_action
@notify_high_value_lead
def add_lead_to_crm(lead):
    print(f"🚀 Lead added to CRM: {lead['name']} at {lead['company']}")
    return lead

leads = [
    {"name": "Sumaiya Ahmed", "company": "Pathao", "position": "CEO", "deal_size": 2_000_000, "industry": "Telecom"},
    {"name": "Tanvir Ahmed", "company": "Grameenphone", "position": "CFO", "deal_size": 800_000, "industry": "Telecom"},
    {"name": "Nusrat Jahan", "company": "bKash", "position": "CEO", "deal_size": 1_500_000, "industry": "FinTech"},
]

# Adding leads to CRM
for lead in leads:
    add_lead_to_crm(lead)
