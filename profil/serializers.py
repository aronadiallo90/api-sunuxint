from rest_framework.serializers import ModelSerializer
 
from profil.models import Profil
 
class ProfilSerializer(ModelSerializer):
 
    class Meta:
        model = Profil
        fields = ['id','profile_photo', 'username','interet','biographie']