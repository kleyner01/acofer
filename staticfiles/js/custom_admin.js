document.addEventListener('DOMContentLoaded', function () {
    const possuiHabilitacaoField = document.querySelector('input[name="possui_habilitacao"]');
    const tipoHabilitacaoField = document.querySelector('.field-tipo_habilitacao');
    const serieCarteiraField = document.querySelector('.field-serie_carteira_profissional');

    function toggleFields() {
        if (possuiHabilitacaoField.checked) {
            tipoHabilitacaoField.style.display = '';
            serieCarteiraField.style.display = '';
        } else {
            tipoHabilitacaoField.style.display = 'none';
            serieCarteiraField.style.display = 'none';
        }
    }

    possuiHabilitacaoField.addEventListener('change', toggleFields);
    toggleFields();  // Chama a função para definir o estado inicial
});
