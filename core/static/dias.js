document.addEventListener('DOMContentLoaded', function () {
            const opcoes = document.querySelectorAll('.opcoes');
            opcoes.forEach(dia => {
                dia.addEventListener('click', function () {
                    const checkbox = document.getElementById(this.getAttribute('for'));
                    this.style.backgroundColor = checkbox.checked ? '#d1a97e' : 'rgba(18, 172, 4, 0.7)';
                });
            });
        });

        // Exemplo de como obter os valores dos checkboxes selecionados de cada formulário:
        document.getElementById('enviarTudo').addEventListener('click', function (event) {
            event.preventDefault();

            // Função para obter valores selecionados de checkboxes
            function getCheckedValues(formId, inputName) {
                return Array.from(document.querySelectorAll(`#${formId} input[name="${inputName}"]:checked`))
                    .map(input => input.value);
            }

            const diaMes = getCheckedValues('diasForm', 'opcoes');
            const mes = getCheckedValues('mesesForm', 'meses');
            const diasSemana = getCheckedValues('semanForm', 'dias_semana');
            const hora = getCheckedValues('horariosForm', 'horarios');

            // Função para exibir toasts
            function showToast(mensagem) {
                const toast = document.getElementById('toast');
                toast.textContent = mensagem;
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 3000);
            }

            // Obtendo reservas do localStorage
            const reservas = JSON.parse(localStorage.getItem('reservas')) || [];

            if (!diaMes.length || !mes.length || !diasSemana.length || !hora.length) {
                showToast('Por favor, selecione pelo menos um dia, mês, dia da semana e horário.');
                return;
            }
            const reservaId = `${diaMes.join(',')}-${mes.join(',')}-${diasSemana.join(',')}-${hora.join(',')}`;

            // Verificando se já existe uma reserva com os mesmos dados
            if (reservas.some(reserva =>
                JSON.stringify(reserva.diaMes) === JSON.stringify(diaMes) &&
                JSON.stringify(reserva.mes) === JSON.stringify(mes) &&
                JSON.stringify(reserva.diasSemana) === JSON.stringify(diasSemana) &&
                JSON.stringify(reserva.hora) === JSON.stringify(hora))) {
                showToast('Já existe uma reserva com esses dados!');
                return;
            }
            // Criando nova reserva
            const reserva = {
                diaMes,
                mes,
                diasSemana,
                hora
            };

            // Salvando reserva no localStorage
            reservas.push(reserva);
            localStorage.setItem('reservas', JSON.stringify(reservas));

            // Exibindo toast de sucesso
            showToast('Reserva cadastrada com sucesso!');

            // Limpando formulários após cadastro
            document.getElementById('diasForm').reset();
            document.getElementById('mesesForm').reset();
            document.getElementById('semanForm').reset();
            document.getElementById('horariosForm').reset();

            // Redirecionando para a página de login após um tempo
            setTimeout(() => {
                window.location.href = '/reservas/';
            }, 3000);
        });