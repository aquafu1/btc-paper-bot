# Paper trading leaderboard (FAKE money)

Updated 2026-11-10 15:57 UTC. Running since 2026-11-09 17:30. Each strategy starts with $1000, bets $10/trade. 28 settled trades (28 at real Polymarket prices).

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | Worst drawdown | Verdict |
|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 3 | 100.0 | 46.7 | $+73.15 | +243.8% | $1073.15 | $0.00 | too few trades |
| value_ev5 | 2 | 100.0 | 21.8 | $+72.77 | +363.9% | $1072.77 | $0.00 | too few trades |
| value_ev10 | 2 | 100.0 | 21.8 | $+72.77 | +363.9% | $1072.77 | $0.00 | too few trades |
| value_ev20 | 2 | 100.0 | 21.8 | $+72.77 | +363.9% | $1072.77 | $0.00 | too few trades |
| coinflip | 4 | 75.0 | 32.2 | $+65.29 | +163.2% | $1065.29 | $10.15 | too few trades |
| always_up | 4 | 50.0 | 55.8 | $+15.38 | +38.5% | $1015.38 | $10.15 | too few trades |
| reversal_60m_0.30pct | 1 | 100.0 | 96.4 | $+0.38 | +3.8% | $1000.38 | $0.00 | too few trades |
| momentum_60m_0.30pct | 1 | 0.0 | 6.1 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |
| trend_filter | 2 | 0.0 | 80.7 | $-20.30 | -101.5% | $979.70 | $20.30 | too few trades |
| momentum_5m_0.00pct | 4 | 25.0 | 70.3 | $-30.07 | -75.2% | $969.93 | $30.07 | too few trades |
| momentum_15m_0.10pct | 3 | 0.0 | 55.8 | $-30.45 | -101.5% | $969.55 | $30.45 | too few trades |

**How to read this:** a strategy makes money only if Win % beats Break-even %. Ignore anything under ~300 trades. It should also clearly beat `coinflip`. "real edge?" means the win rate is 2+ standard errors above break-even -- still check it holds for another week before trusting it.
