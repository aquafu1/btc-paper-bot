# Paper trading leaderboard (FAKE money)

Updated 2026-11-10 00:51 UTC. Running since 2026-11-09 17:30. Each strategy starts with $1000, bets $10/trade. 10 settled trades (10 at real Polymarket prices).

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | Worst drawdown | Verdict |
|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 1 | 100.0 | 96.4 | $+0.38 | +3.8% | $1000.38 | $0.00 | too few trades |
| reversal_60m_0.30pct | 1 | 100.0 | 96.4 | $+0.38 | +3.8% | $1000.38 | $0.00 | too few trades |
| coinflip | 2 | 50.0 | 42.6 | $-7.48 | -37.4% | $992.52 | $10.15 | too few trades |
| always_up | 2 | 50.0 | 59.9 | $-9.77 | -48.9% | $990.23 | $10.15 | too few trades |
| momentum_5m_0.00pct | 2 | 50.0 | 59.9 | $-9.77 | -48.9% | $990.23 | $10.15 | too few trades |
| momentum_15m_0.10pct | 1 | 0.0 | 6.1 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |
| momentum_60m_0.30pct | 1 | 0.0 | 6.1 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |

**How to read this:** a strategy makes money only if Win % beats Break-even %. Ignore anything under ~300 trades. It should also clearly beat `coinflip`. "real edge?" means the win rate is 2+ standard errors above break-even -- still check it holds for another week before trusting it.
