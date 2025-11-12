from datetime import datetime
from django.core.mail import send_mail
from orders.models import Order

def send_daily_sales_report():
    """Generate and email a daily sales report."""
    today = datetime.now().date()
    total_orders = Order.objects.filter(created_at__date=today).count()
    send_mail(
        subject=f"Daily Sales Report – {today}",
        message=f"Total Orders Today: {total_orders}",
        from_email="noreply@ecommerce.com",
        recipient_list=["admin@ecommerce.com"],
    )
    print(f"[CRON] Sent daily report for {today}")
