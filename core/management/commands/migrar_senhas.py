from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Usuarios

class Command(BaseCommand):
    help = 'Converte senhas existentes em texto puro para formato hash'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando migração de senhas...')
        
        # Conta quantos usuários precisam ser atualizados
        usuarios = Usuarios.objects.all()
        total = usuarios.count()
        
        if total == 0:
            self.stdout.write(self.style.WARNING('Nenhum usuário encontrado no banco de dados.'))
            return
            
        self.stdout.write(f'Encontrados {total} usuários para atualizar.')
        
        # Usa uma transação para garantir que todas as senhas sejam atualizadas ou nenhuma
        with transaction.atomic():
            for i, usuario in enumerate(usuarios, 1):
                # Pega a senha atual (em texto puro)
                senha_atual = usuario.senha
                
                # Usa set_password para criar o hash e salva a alteração
                usuario.set_password(senha_atual)
                usuario.save(update_fields=['senha'])
                
                # Mostra progresso
                self.stdout.write(f'Processando usuário {i} de {total}: {usuario.nome}')
        
        self.stdout.write(self.style.SUCCESS(f'Migração completa! {total} usuários atualizados com sucesso.'))