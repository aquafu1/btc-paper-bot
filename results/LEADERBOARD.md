# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1156 windows, 31928 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 614 | 34.5 | 35.2 | $-397.85 | -6.5% | $602.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1504 | 38.3 | 39.2 | $-871.63 | -5.8% | $128.37 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3205 | 50.8 | 50.4 | $-1071.17 | -3.3% | $-71.17 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2693 | 49.8 | 49.5 | $-1125.95 | -4.2% | $-125.95 | -2.2 | done | losing for real |
| value_ev5 | 2275 | 40.2 | 41.1 | $-1260.59 | -5.5% | $-260.59 | -2.2 | done | losing for real |
| trend_filter | 1891 | 49.1 | 50.5 | $-1497.05 | -7.9% | $-497.05 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2693 | 50.2 | 51.0 | $-1740.43 | -6.5% | $-740.43 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3205 | 49.2 | 50.2 | $-1923.02 | -6.0% | $-923.02 | -3.4 | done | losing for real |
| coinflip | 4616 | 50.2 | 50.2 | $-1950.12 | -4.2% | $-950.12 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4616 | 50.1 | 51.4 | $-2936.07 | -6.4% | $-1936.07 | -4.5 | done | losing for real |
| always_up | 4616 | 47.7 | 49.3 | $-3557.02 | -7.7% | $-2557.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7316 | 48.2 | 49.0 | $-3875.91 |
| ETH | 7913 | 48.1 | 48.4 | $-4682.64 |
| SOL | 8310 | 48.0 | 48.4 | $-4684.15 |
| XRP | 8389 | 48.1 | 48.2 | $-5088.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
