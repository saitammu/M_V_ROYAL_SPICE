from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_seed_fixed_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='tracker.vendor')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('vendor', 'date')},
            },
        ),
    ]
