# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1624 windows, 39042 settled trades, 349 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 826 | 34.4 | 35.2 | $-612.08 | -7.4% | $387.92 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3848 | 50.8 | 50.0 | $-1024.52 | -2.7% | $-24.52 | -1.6 | done | can't tell from luck |
| value_ev10 | 1955 | 38.3 | 39.0 | $-1105.41 | -5.7% | $-105.41 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3218 | 51.1 | 50.9 | $-1475.66 | -4.6% | $-475.66 | -2.7 | done | losing for real |
| value_ev5 | 2923 | 40.4 | 41.0 | $-1535.82 | -5.3% | $-535.82 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3218 | 48.9 | 49.2 | $-1751.56 | -5.4% | $-751.56 | -3.1 | done | losing for real |
| trend_filter | 2289 | 48.5 | 50.4 | $-2023.76 | -8.8% | $-1023.76 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3848 | 49.2 | 50.2 | $-2345.19 | -6.1% | $-1345.19 | -3.8 | done | losing for real |
| coinflip | 5639 | 50.1 | 49.9 | $-2345.55 | -4.2% | $-1345.55 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5639 | 50.2 | 51.3 | $-3442.99 | -6.1% | $-2442.99 | -4.7 | done | losing for real |
| always_up | 5639 | 48.2 | 49.1 | $-3595.42 | -6.4% | $-2595.42 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10429 | 47.9 | 48.6 | $-5922.82 |
| ETH | 11303 | 48.0 | 47.7 | $-5750.92 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
