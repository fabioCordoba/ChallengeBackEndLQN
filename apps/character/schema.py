from apps.character.models.character import Character
import graphene
from graphene_django.types import DjangoObjectType


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = "__all__"

class CharacterQuery(graphene.ObjectType):
    all_characters = graphene.List(CharacterType)
    character_by_id = graphene.Field(CharacterType, id=graphene.UUID(required=True))

    def resolve_all_characters(root, info):
        return Character.objects.all()
    
    def resolve_character_by_id(root, info, id):
        try:
            return Character.objects.get(id=id)
        except Character.DoesNotExist:
            return None
