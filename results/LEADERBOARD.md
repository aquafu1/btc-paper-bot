# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1099 windows, 30402 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 577 | 34.7 | 35.0 | $-321.49 | -5.6% | $678.51 | -1.0 | done | can't tell from luck |
| value_ev10 | 1413 | 38.2 | 39.1 | $-811.09 | -5.7% | $188.91 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3069 | 51.1 | 50.5 | $-868.54 | -2.8% | $131.46 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2583 | 49.7 | 49.4 | $-1110.95 | -4.3% | $-110.95 | -2.2 | done | losing for real |
| value_ev5 | 2144 | 40.1 | 41.0 | $-1180.70 | -5.5% | $-180.70 | -2.2 | done | losing for real |
| trend_filter | 1800 | 49.3 | 50.5 | $-1327.14 | -7.4% | $-327.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2583 | 50.3 | 51.1 | $-1634.62 | -6.3% | $-634.62 | -3.3 | done | losing for real |
| coinflip | 4388 | 50.5 | 50.2 | $-1651.89 | -3.8% | $-651.89 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3069 | 48.9 | 50.2 | $-1998.77 | -6.5% | $-998.77 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4388 | 50.8 | 51.4 | $-2257.76 | -5.1% | $-1257.76 | -3.5 | done | losing for real |
| always_up | 4388 | 47.5 | 49.3 | $-3509.01 | -8.0% | $-2509.01 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6958 | 48.4 | 49.0 | $-3355.12 |
| ETH | 7531 | 48.2 | 48.4 | $-4427.56 |
| SOL | 7914 | 48.1 | 48.4 | $-4342.43 |
| XRP | 7999 | 48.2 | 48.2 | $-4546.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
