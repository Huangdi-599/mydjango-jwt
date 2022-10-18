from rest_framework import serializers
from .models import student, Owner, school


class studentserial(serializers.ModelSerializer):
    class Meta:
        model = student 
        fields = [
            
            'id',
            'name', 'age'
        ]
        

class schoolserial(serializers.ModelSerializer):
    class Meta:
        model = school 
        fields = [
            'id',
            'name',
            'description',
            'country',
            'state'
        ]
                
        
class UserSerial(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    email = serializers.EmailField(write_only = True)
    class Meta:
        model = Owner
        fields = [
            'id',
            'username',
            'password',
            'email',
            'name',
        ]
        
    #encrypting password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    #Validating email inputted 
    def validate_email(self, value):
        request =  self.context.get('request')
        query = Owner.objects.filter(email__iexact = value)
        if query.exists():
            raise serializers.ValidationError("This email address already exist")
        return value
            