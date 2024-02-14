
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.AddField(
            model_name='student',
            name='phoneNumber',
            field=models.IntegerField(null=True),
        ),
    ]
