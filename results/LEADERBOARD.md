# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 431 windows, 11850 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 214 | 34.6 | 36.2 | $-174.42 | -8.2% | $825.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1012 | 50.8 | 50.0 | $-263.64 | -2.6% | $736.36 | -0.8 | done | can't tell from luck |
| value_ev10 | 555 | 39.1 | 40.3 | $-365.64 | -6.6% | $634.36 | -1.3 | done | can't tell from luck |
| trend_filter | 681 | 49.8 | 50.7 | $-397.02 | -5.8% | $602.98 | -1.6 | done | can't tell from luck |
| value_ev5 | 832 | 41.3 | 42.1 | $-451.13 | -5.4% | $548.87 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1198 | 49.2 | 50.0 | $-624.56 | -5.2% | $375.44 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1198 | 50.8 | 51.8 | $-709.13 | -5.9% | $290.87 | -2.2 | done | losing for real |
| coinflip | 1716 | 50.5 | 50.9 | $-762.36 | -4.4% | $237.64 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1012 | 49.2 | 51.9 | $-937.52 | -9.3% | $62.48 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1716 | 49.6 | 51.6 | $-1266.72 | -7.4% | $-266.72 | -3.2 | done | losing for real |
| always_up | 1716 | 46.4 | 50.6 | $-2027.59 | -11.8% | $-1027.59 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2678 | 47.6 | 49.4 | $-2011.91 |
| ETH | 2973 | 48.0 | 48.9 | $-1878.37 |
| SOL | 3077 | 47.9 | 49.4 | $-2365.34 |
| XRP | 3122 | 48.7 | 49.3 | $-1724.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
