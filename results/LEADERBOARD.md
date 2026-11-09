# Paper trading leaderboard (FAKE money)

Updated 2026-11-09 17:50 UTC. Running since 2026-11-09 17:30. Each strategy starts with $1000, bets $10/trade. 3 settled trades (3 at real Polymarket prices).

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | Worst drawdown | Verdict |
|---|---|---|---|---|---|---|---|---|
| coinflip | 1 | 100.0 | 79.2 | $+2.67 | +26.7% | $1002.67 | $0.00 | too few trades |
| always_up | 1 | 0.0 | 23.3 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |
| momentum_5m_0.00pct | 1 | 0.0 | 23.3 | $-10.15 | -101.5% | $989.85 | $10.15 | too few trades |

**How to read this:** a strategy makes money only if Win % beats Break-even %. Ignore anything under ~300 trades. It should also clearly beat `coinflip`. "real edge?" means the win rate is 2+ standard errors above break-even -- still check it holds for another week before trusting it.
