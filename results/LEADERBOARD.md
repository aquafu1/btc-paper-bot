# Paper trading leaderboard (FAKE money)

Updated 2026-11-10 07:54 UTC. Running since 2026-11-09 17:30. Each strategy starts with $1000, bets $10/trade. 19 settled trades (19 at real Polymarket prices).

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | Worst drawdown | Verdict |
|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 2 | 100.0 | 59.4 | $+35.68 | +178.4% | $1035.68 | $0.00 | too few trades |
| value_ev5 | 1 | 100.0 | 22.3 | $+35.30 | +353.0% | $1035.30 | $0.00 | too few trades |
| value_ev10 | 1 | 100.0 | 22.3 | $+35.30 | +353.0% | $1035.30 | $0.00 | too few trades |
| value_ev20 | 1 | 100.0 | 22.3 | $+35.30 | +353.0% | $1035.30 | $0.00 | too few trades |
| coinflip | 3 | 66.7 | 35.9 | $+27.82 | +92.7% | $1027.83 | $10.15 | too few trades |
| always_up | 3 | 66.7 | 47.4 | $+25.53 | +85.1% | $1025.53 | $10.15 | too few trades |
| reversal_60m_0.30pct | 1 | 100.0 | 96.4 | $+0.38 | +3.8% | $1000.38 | $0.00 | too few trades |
| momentum_60m_0.30pct | 1 | 0.0 | 6.1 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |
| trend_filter | 1 | 0.0 | 80.2 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |
| momentum_5m_0.00pct | 3 | 33.3 | 66.7 | $-19.92 | -66.4% | $980.08 | $19.92 | too few trades |
| momentum_15m_0.10pct | 2 | 0.0 | 43.1 | $-20.30 | -101.5% | $979.70 | $20.30 | too few trades |

**How to read this:** a strategy makes money only if Win % beats Break-even %. Ignore anything under ~300 trades. It should also clearly beat `coinflip`. "real edge?" means the win rate is 2+ standard errors above break-even -- still check it holds for another week before trusting it.
