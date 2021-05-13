from rest_framework import status
from rest_framework.test import APITestCase

class EquipoTests(APITestCase):

    fixtures = ['api/fixtures/fixtures.json']
            
    def test_equipos_list(self):
        """
        Permite probar la lista de equipos.
        """
        response = self.client.get('/api/equipos/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        
    def test_buscar_equipo_por_nombre(self):
        """
        Permite probar el filtro de equipo por nombre
        """
        response = self.client.get('/api/equipos/', {'nombre': 'Barcelona, FC'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)        
        
    def test_buscar_equipo_por_ciudad(self):
        """
        Permite probar el filtro de equipo por ciudad
        """
        response = self.client.get('/api/equipos/', {'ciudad': 'Madrid'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
    
    # TODO: no esta guardando
    def test_crear_equipo(self):
        """
        Permite probar el filtro de equipo por ciudad
        """
        response = self.client.post('/api/equipos/', {'name': 'Atlético de Madrid', 'city': 'Madrid'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class JugadorTests(APITestCase):

    fixtures = ['api/fixtures/fixtures.json']
            
    def test_equipos_list(self):
        """
        Permite probar la lista de jugadores.
        """
        response = self.client.get('/api/jugadores/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),4)
        
    def test_buscar_jugador_por_nombre(self):
        """
        Permite probar el filtro de jugador por nombre
        """
        response = self.client.get('/api/jugadores/', {'nombre': 'Leonel Messi'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)        
        
    def test_buscar_jugador_por_goles(self):
        """
        Permite probar el filtro de jugador por cantidad de goles
        """
        response = self.client.get('/api/equipos/', {'goles': 31}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        
    def test_buscar_jugador_por_equipo(self):
        """
        Permite probar el filtro de jugador por cantidad de goles
        """
        response = self.client.get('/api/equipos/', {'equipo': 'Real Madrid'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
                        