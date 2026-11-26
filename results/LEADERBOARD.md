# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1470 windows, 37050 settled trades, 359 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 749 | 34.0 | 35.4 | $-623.47 | -8.3% | $376.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1805 | 38.4 | 39.2 | $-980.25 | -5.4% | $19.75 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3694 | 50.9 | 50.1 | $-1000.60 | -2.7% | $-0.60 | -1.6 | done | can't tell from luck |
| value_ev5 | 2721 | 40.4 | 41.1 | $-1441.14 | -5.3% | $-441.14 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3099 | 49.2 | 49.2 | $-1514.12 | -4.9% | $-514.12 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3099 | 50.8 | 51.0 | $-1603.76 | -5.2% | $-603.76 | -3.0 | done | losing for real |
| trend_filter | 2199 | 48.7 | 50.3 | $-1855.16 | -8.4% | $-855.16 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3694 | 49.1 | 50.2 | $-2292.21 | -6.2% | $-1292.21 | -3.8 | done | losing for real |
| coinflip | 5330 | 49.9 | 50.0 | $-2436.46 | -4.6% | $-1436.46 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 5330 | 50.2 | 51.3 | $-3323.57 | -6.2% | $-2323.57 | -4.7 | done | losing for real |
| always_up | 5330 | 48.1 | 49.2 | $-3529.43 | -6.6% | $-2529.43 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9517 | 48.0 | 48.7 | $-5232.14 |
| ETH | 10223 | 47.9 | 48.0 | $-5783.82 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
