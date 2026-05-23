// PUBLICAÇÃO DO PAMPA MOVSTOCK
//
// PASSO A PASSO PARA GERAR O LINK ONLINE:
//
// 1. Criar conta gratuita no Streamlit Cloud
// 2. Subir este projeto no GitHub
// 3. Conectar repositório ao Streamlit
// 4. Publicar aplicação
// 5. Gerar link compartilhável para equipe comercial
//
// Exemplo de link:
// https://pampa.movstock.app
//
// Estrutura recomendada:
// - Front-end React
// - Banco de dados Excel/Google Sheets
// - Atualização automática de estoque
// - Dashboard comercial
// - Busca inteligente
//
// Próxima evolução:
// - login por vendedor
// - ranking de oportunidades
// - IA comercial
// - aplicativo Android/iPhone
//
export default function MovstockApp() {
  const pecas = [
    {
      codigo: '71413325',
      descricao: 'Disco de Grade Recortado',
      aplicacao: 'MF 6713 | MF 7720 | Valtra BH 180',
      estoque: 18,
      filial: 'Cuiabá',
      clientes: ['Fazenda Santa Luzia', 'Grupo Araguaia'],
    },
    {
      codigo: '6269371M91',
      descricao: 'Conjunto Rolamento',
      aplicacao: 'MF 4292 | MF 5275',
      estoque: 9,
      filial: 'Nova Olímpia',
      clientes: ['Agropecuária Vitória'],
    },
    {
      codigo: 'F75 6F',
      descricao: 'Disco Corte 16x4,5mm',
      aplicacao: 'Plantadeiras Massey Ferguson',
      estoque: 31,
      filial: 'Tangará da Serra',
      clientes: ['Fazenda Horizonte'],
    },
  ]

  return (
    <div className="min-h-screen bg-black text-white overflow-hidden">
      <div className="fixed inset-0 pointer-events-none opacity-20">
        <div className="absolute top-0 left-0 w-[500px] h-[500px] bg-red-700 rounded-full blur-3xl"></div>
        <div className="absolute bottom-0 right-0 w-[400px] h-[400px] bg-red-900 rounded-full blur-3xl"></div>
      </div>
      {/* Header */}
      <div className="bg-gradient-to-r from-red-700 via-red-600 to-black p-6 shadow-2xl">
        <div className="max-w-7xl mx-auto flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className="h-16 w-16 rounded-3xl bg-white/10 backdrop-blur-xl border border-white/20 flex items-center justify-center shadow-2xl">
              <span className="text-3xl">🚜</span>
            </div>
            <div>
            <h1 className="text-5xl font-black tracking-wide bg-gradient-to-r from-white via-red-200 to-red-500 bg-clip-text text-transparent">PAMPA MOVSTOCK</h1>
            <p className="text-red-100 text-lg mt-2">
              Inteligência Comercial para Peças Agrícolas
            </p>
          </div>

          <div className="flex gap-3 flex-wrap">
            <button className="bg-white text-red-700 px-5 py-3 rounded-2xl font-bold shadow-xl hover:scale-105 transition-all">
              Dashboard
            </button>
            <button className="bg-red-900 px-5 py-3 rounded-2xl font-semibold border border-red-500 hover:bg-red-800 transition-all">
              Estoque
            </button>
            <button className="bg-red-900 px-5 py-3 rounded-2xl font-semibold border border-red-500 hover:bg-red-800 transition-all">
              Clientes
            </button>
          </div>
        </div>
      </div>

      {/* Hero */}
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1500937386664-56d1dfef3854?q=80&w=1600&auto=format&fit=crop')] bg-cover bg-center opacity-20"></div>

        <div className="relative max-w-7xl mx-auto px-6 py-16">
          <div className="grid lg:grid-cols-2 gap-10 items-center">
            <div>
              <div className="inline-flex items-center gap-2 bg-red-700/30 border border-red-500 px-4 py-2 rounded-full mb-6">
                <span className="h-3 w-3 bg-red-500 rounded-full"></span>
                <span className="text-sm font-semibold tracking-wide">
                  Plataforma Inteligente Agro
                </span>
              </div>

              <h2 className="text-6xl font-black leading-tight mb-6">
                O estoque virou
                <span className="text-red-500"> oportunidade.</span>
              </h2>

              <p className="text-gray-300 text-xl leading-relaxed mb-8">
                Conecte peças agrícolas, aplicações, estoque e clientes em um único sistema inteligente.
              </p>

              <div className="flex flex-wrap gap-4">
                <button className="bg-red-600 hover:bg-red-500 px-8 py-4 rounded-2xl text-lg font-bold shadow-2xl transition-all hover:scale-105">
                  Iniciar Busca
                </button>

                <button className="border border-gray-600 hover:border-red-500 px-8 py-4 rounded-2xl text-lg font-semibold transition-all">
                  Ver Dashboard
                </button>
              </div>
            </div>

            <div>
              <div className="bg-zinc-900/80 backdrop-blur-xl rounded-3xl p-6 border border-zinc-700 shadow-2xl">
                <div className="flex items-center justify-between mb-6">
                  <h3 className="text-2xl font-bold">Busca Inteligente</h3>
                  <div className="bg-red-600 px-3 py-1 rounded-full text-sm font-bold">
                    ONLINE
                  </div>
                </div>

                <input
                  placeholder="Digite código, modelo, grupo ou cliente"
                  className="w-full bg-zinc-800 border border-zinc-600 rounded-2xl p-4 text-lg mb-6 outline-none focus:border-red-500"
                />

                <div className="grid grid-cols-2 gap-4 mb-6">
                  <button className="bg-zinc-800 hover:bg-red-700 transition-all rounded-2xl p-4 font-semibold border border-zinc-700">
                    Código
                  </button>
                  <button className="bg-zinc-800 hover:bg-red-700 transition-all rounded-2xl p-4 font-semibold border border-zinc-700">
                    Modelo
                  </button>
                  <button className="bg-zinc-800 hover:bg-red-700 transition-all rounded-2xl p-4 font-semibold border border-zinc-700">
                    Grupo
                  </button>
                  <button className="bg-zinc-800 hover:bg-red-700 transition-all rounded-2xl p-4 font-semibold border border-zinc-700">
                    Cliente
                  </button>
                </div>

                <button className="w-full bg-red-600 hover:bg-red-500 transition-all rounded-2xl py-4 text-xl font-black shadow-xl">
                  BUSCAR
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Dashboard Cards */}
      <div className="max-w-7xl mx-auto px-6 py-10 relative z-10">
        <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-6">
          {[
            ['R$ 4.8 Mi', 'Valor em Estoque'],
            ['1.284', 'Peças Aplicadas'],
            ['486', 'Clientes Relacionados'],
            ['92%', 'Busca Inteligente'],
          ].map((item, index) => (
            <div
              key={index}
              className="relative overflow-hidden bg-gradient-to-br from-zinc-900 via-zinc-800 to-black border border-zinc-700 rounded-[32px] p-7 shadow-[0_0_40px_rgba(255,0,0,0.15)] hover:border-red-500 hover:-translate-y-2 transition-all duration-300"
            >
              <div className="text-5xl font-black text-red-500 mb-3 tracking-tight">
                {item[0]}
              </div>
              <div className="text-gray-300 font-medium text-lg">
                {item[1]}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Resultados */}
      <div className="max-w-7xl mx-auto px-6 py-12">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="text-4xl font-black mb-2">
              Resultados Inteligentes
            </h2>
            <p className="text-gray-400 text-lg">
              Estoque conectado com oportunidades comerciais.
            </p>
          </div>

          <div className="bg-red-600 px-5 py-3 rounded-2xl font-bold shadow-xl">
            PAMPA MOVSTOCK AI
          </div>
        </div>

        <div className="space-y-6">
          {pecas.map((peca, index) => (
            <div
              key={index}
              className="bg-zinc-900 border border-zinc-700 rounded-3xl overflow-hidden hover:border-red-500 transition-all shadow-2xl"
            >
              <div className="grid lg:grid-cols-4 gap-6 p-6">
                <div>
                  <div className="text-sm uppercase tracking-widest text-red-500 mb-2 font-bold">
                    Código
                  </div>
                  <div className="text-3xl font-black">{peca.codigo}</div>
                </div>

                <div>
                  <div className="text-sm uppercase tracking-widest text-red-500 mb-2 font-bold">
                    Descrição
                  </div>
                  <div className="text-xl font-semibold text-gray-200">
                    {peca.descricao}
                  </div>
                </div>

                <div>
                  <div className="text-sm uppercase tracking-widest text-red-500 mb-2 font-bold">
                    Aplicações
                  </div>
                  <div className="text-gray-300 leading-relaxed">
                    {peca.aplicacao}
                  </div>
                </div>

                <div className="flex flex-col justify-between">
                  <div>
                    <div className="text-sm uppercase tracking-widest text-red-500 mb-2 font-bold">
                      Estoque
                    </div>
                    <div className="text-4xl font-black text-green-400">
                      {peca.estoque}
                    </div>
                  </div>

                  <div className="mt-4 bg-red-600/20 border border-red-600 rounded-2xl px-4 py-2 text-center font-bold">
                    {peca.filial}
                  </div>
                </div>
              </div>

              <div className="border-t border-zinc-800 px-6 py-5 bg-zinc-950">
                <div className="flex flex-wrap gap-3 items-center">
                  <div className="text-red-500 font-bold uppercase tracking-wider">
                    Clientes Potenciais:
                  </div>

                  {peca.clientes.map((cliente, i) => (
                    <div
                      key={i}
                      className="bg-zinc-800 border border-zinc-700 rounded-full px-4 py-2 font-medium hover:border-red-500 transition-all"
                    >
                      {cliente}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Footer */}
      <div className="border-t border-zinc-800 mt-16">
        <div className="max-w-7xl mx-auto px-6 py-10 flex flex-col lg:flex-row justify-between items-center gap-4">
          <div>
            <div className="text-3xl font-black text-red-500">PAMPA MOVSTOCK</div>
            <div className="text-gray-500 mt-2">
              Plataforma Inteligente de Peças Agrícolas
            </div>
          </div>

          <div className="text-gray-400 text-center lg:text-right">
            Projeto desenvolvido para inteligência comercial agro.
            <br />
            Layout premium inspirado no universo Massey Ferguson.
          </div>
        </div>
      </div>
    </div>
  )
}

