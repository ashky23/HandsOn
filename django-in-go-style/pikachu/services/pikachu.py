import uuid
from pikachu.dto.pikachu import PikachuObject, PikachuResponseObject
from pikachu.models import Pikachu

class PikachuService:
    def create_pikachu(self, pikachu_data: PikachuObject) -> Pikachu:
        pikachu_instance = Pikachu.objects.create(
            name=pikachu_data.name,
            is_admin=pikachu_data.is_admin,
            age=pikachu_data.age
            )
        return pikachu_instance
        
    def update_pikachu(self, pikachu_id: uuid.UUID, pikachu_data: PikachuObject) -> Pikachu:
        pikachu_instance = Pikachu.objects.get(id=pikachu_id)
        pikachu_instance.name = pikachu_data.name
        pikachu_instance.is_admin = pikachu_data.is_admin
        pikachu_instance.age = pikachu_data.age
        pikachu_instance.save()
        return pikachu_instance
    
    def list_pikachu(self, pikachu_instances: list[Pikachu]) -> list[PikachuObject]:
        return [self._get_pikachu_response_object(pikachu_instance) for pikachu_instance in pikachu_instances]
    
    def retrieve_pikachu(self, pikachu_instance: Pikachu) -> PikachuResponseObject:
        return self._get_pikachu_response_object(pikachu_instance)
    
    def delete_pikachu(self, pikachu_id: uuid.UUID, pikachu_data: PikachuObject) -> None:
        Pikachu.objects.filter(id = pikachu_id).delete()
        
    def _get_pikachu_response_object(self, pikachu_instance: Pikachu) -> PikachuResponseObject:
        return PikachuResponseObject(
            id=str(pikachu_instance.id),
            name=pikachu_instance.name,
            age=pikachu_instance.age,
            is_admin=pikachu_instance.is_admin,
            created_at=str(pikachu_instance.created_at),
            updated_at=str(pikachu_instance.updated_at)
        )
        