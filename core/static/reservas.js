// Recupera as reservas do localStorage ou inicializa como array vazio
        let reservas = JSON.parse(localStorage.getItem('reservas')) || [];

        function renderReservas() {
    const tableBody = document.getElementById('reservasTableBody');
    tableBody.innerHTML = ''; // Limpa o conteúdo atual

    const meses = {
        'Janeiro': 1,
        'Fevereiro': 2,
        'Março': 3,
        'Abril': 4,
        'Maio': 5,
        'Junho': 6,
        'Julho': 7,
        'Agosto': 8,
        'Setembro': 9,
        'Outubro': 10,
        'Novembro': 11,
        'Dezembro': 12
    };

    // Ordena as reservas por mês, dia e hora
    reservas.sort((a, b) => {
        const mesA = meses[a.mes] || 0;
        const mesB = meses[b.mes] || 0;
        if (mesA !== mesB) return mesA - mesB;

        const diaA = parseInt(a.diaMes);
        const diaB = parseInt(b.diaMes);
        if (diaA !== diaB) return diaA - diaB;
    });

    // Renderiza as linhas
    reservas.forEach((reserva, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${reserva.diaMes}</td>
            <td>${reserva.mes}</td>
            <td>${reserva.diasSemana}</td>
            <td>${reserva.hora}</td>
            <td>
                <button class="btn btn-danger" onclick="cancelarReserva(${index})">Cancelar</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

        function cancelarReserva(index) {
            if (confirm('Tem certeza que deseja cancelar esta reserva?')) {
                reservas.splice(index, 1); // Remove a reserva do array
                localStorage.setItem('reservas', JSON.stringify(reservas)); // Atualiza o localStorage
                renderReservas(); // Re-renderiza a tabela
            }
        }
        // Renderiza as reservas ao carregar a página
        document.addEventListener('DOMContentLoaded', renderReservas);