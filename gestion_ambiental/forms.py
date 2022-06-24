from django.forms import ValidationError

from gestion_ambiental.models import EvidenciaGestionAmbiental

from bootstrap_modal_forms.forms import BSModalModelForm


class EvidenciaGestionAmbientalForm(BSModalModelForm):

    class Meta:
        model = EvidenciaGestionAmbiental
        fields = ['nombre_evidencia', 'formato']


    def clean_formato(self, **kwargs):
        CONTENT_TYPES = ['pdf','png']
        # 2.5MB - 2621440
        # 5MB - 5242880
        # 10MB - 10485760
        # 20MB - 20971520
        # 50MB - 5242880
        # 100MB 104857600
        # 250MB - 214958080
        # 500MB - 429916160
        MAX_UPLOAD_SIZE = "2621440"
        data = self.cleaned_data
        formato = data['formato']
        content_type = formato.content_type.split('/')[1]
        if content_type in CONTENT_TYPES:
            if formato.size > int(MAX_UPLOAD_SIZE):
                raise ValidationError('El archivo supera los dos 2,5 MB Intenta nuevamente')
        else:
            raise ValidationError('Formato de archivo no válido')
        return formato