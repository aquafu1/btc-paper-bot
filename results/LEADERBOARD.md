# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 939 windows, 25991 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 477 | 35.0 | 34.8 | $-165.74 | -3.5% | $834.26 | -0.6 | done | can't tell from luck |
| value_ev10 | 1176 | 38.1 | 39.1 | $-666.59 | -5.7% | $333.41 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2656 | 51.1 | 50.6 | $-862.48 | -3.2% | $137.52 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2221 | 50.2 | 49.9 | $-933.22 | -4.2% | $66.78 | -2.0 | done | can't tell from luck |
| trend_filter | 1545 | 50.0 | 51.0 | $-1078.97 | -7.0% | $-78.97 | -2.8 | done | losing for real |
| value_ev5 | 1786 | 39.7 | 41.0 | $-1123.09 | -6.3% | $-123.09 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2221 | 49.8 | 50.9 | $-1560.47 | -7.0% | $-560.47 | -3.4 | done | losing for real |
| coinflip | 3751 | 50.4 | 50.4 | $-1580.26 | -4.2% | $-580.26 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2656 | 48.9 | 50.3 | $-1751.87 | -6.6% | $-751.87 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3751 | 50.9 | 51.6 | $-1939.05 | -5.2% | $-939.05 | -3.3 | done | losing for real |
| always_up | 3751 | 46.7 | 49.7 | $-3866.77 | -10.3% | $-2866.77 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5919 | 48.2 | 49.1 | $-3475.55 |
| ETH | 6465 | 48.2 | 48.6 | $-4056.98 |
| SOL | 6781 | 48.1 | 48.6 | $-4022.36 |
| XRP | 6826 | 48.3 | 48.5 | $-3973.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
