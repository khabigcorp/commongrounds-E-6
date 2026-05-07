from django.forms import inlineformset_factory
from django import forms
from .models import Commission, Job, JobApplication

JobFormSet = inlineformset_factory(
    Commission,
    Job,
    fields=["role", "manpower_required", "status"],
    extra=0,
    can_delete=True,
)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = [
            "title",
            "maker",
            "commission_type",
            "description",
            "people_required",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        disabled_fields = ["maker"]

        for disabled_field in disabled_fields:
            self.fields[disabled_field].disabled = True
        for field_name in self.fields:
            if field_name not in disabled_fields:
                self.fields[field_name].required = True
