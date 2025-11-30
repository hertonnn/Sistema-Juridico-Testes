import unittest
from datetime import datetime
from sistemaJuridico import (
    Processo, Advogado, Juiz, Tramite, Decisao
)

class TestSistemaJuridico(unittest.TestCase):

    def setUp(self):
        """
        Criando instâncias básicas para evitar repetição de código
        """
        self.processo = Processo(numero="5002025.8.24.0038", assunto="Danos Morais")
        self.advogado = Advogado("Dr. Silva", "123.456.789-00", "silva@law.com", "OAB/SC 12345")
        self.juiz = Juiz("Juiz Moro", "987.654.321-00", "moro@jus.br", "MAT-999", "Entrância Especial")

    def test_fluxo_observer_notificacao(self):
        """
        Verifica se o advogado (o observer) recebe notificação quando o processo (o subject) é movimentado
        """
        self.processo.anexar(self.advogado)
        tramite = Tramite("Despacho", "Aguardando manifestação") 
        self.processo.adicionar_tramite(tramite)
        
        # Teste
        self.assertIn(
            f"Novo trâmite no processo {self.processo.numero}: Despacho", 
            self.advogado.notificacoes,
            "O padrão Observer falhou: O advogado não recebeu a notificação do trâmite."
        )
        

    def test_ciclo_vida_julgamento_encerramento(self):
        """
        Testa boa parte do processo de encerramento de um processo. 
        """
        decisao = Decisao(resultado="Procedente", texto_integral="O réu deve pagar indenização.")
        
        self.juiz.julgar(self.processo, decisao)
        
        # Testes
        self.assertEqual(self.processo.status, "Encerrado", "O processo deveria estar com status Encerrado após julgamento.")
        self.assertIsNotNone(self.processo.data_encerramento, "A data de encerramento não foi registrada.")
        
        ultimo_tramite = self.processo.tramites[-1] # Pega o último tramite da lista
        # Ao julgar, um novo tramite é criado do tipo Julgamento, usando decisão em sua descrição.
        self.assertEqual(ultimo_tramite.tipo, "Julgamento") 
        self.assertIn("Procedente", ultimo_tramite.descricao)

    def test_factory_method_documento(self):
        """
        Testa o Padrão Factory Method implementado em Tramite
        """
        tramite = Tramite("Petição", "Petição inicial do autor")
        
        doc = tramite.gerar_documento("PDF", "Conteúdo binário simulado")
        
        self.assertEqual(doc.tipo, "PDF")
        self.assertEqual(tramite.documento_anexo, doc, "O documento criado não foi vinculado ao trâmite.")
        self.assertTrue(doc.validar_formato()) 

    def test_agendamento_audiencia(self):
        """
        Testa o agendamento de audiência e vinculo com o processo
        """
        data_audiencia = datetime(2025, 12, 1, 14, 0)
        audiencia = self.processo.agendar_audiencia(data_audiencia, "Sala 1", "Conciliação")
        
        self.assertIn(audiencia, self.processo.audiencias)
        self.assertEqual(audiencia.status, "Agendada")

    def test_validacao_processo_ja_encerrado(self):
        """
        Tenta encerrar um processo que já está encerrado e estourar um erro esperado
        """
        self.processo.status = "Encerrado"
        
        with self.assertRaises(ValueError):
            self.processo.encerrar_processo()

if __name__ == '__main__':
    unittest.main()