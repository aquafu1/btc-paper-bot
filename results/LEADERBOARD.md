# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1315 windows, 34913 settled trades, 404 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 687 | 34.2 | 35.3 | $-530.82 | -7.7% | $469.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1685 | 38.8 | 39.2 | $-782.80 | -4.6% | $217.20 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3497 | 50.8 | 50.2 | $-1032.48 | -3.0% | $-32.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 2541 | 40.5 | 41.1 | $-1266.90 | -5.0% | $-266.90 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2933 | 49.4 | 49.4 | $-1393.59 | -4.8% | $-393.59 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2933 | 50.6 | 50.9 | $-1579.18 | -5.4% | $-579.18 | -3.0 | done | losing for real |
| trend_filter | 2077 | 48.8 | 50.5 | $-1752.39 | -8.4% | $-752.39 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3497 | 49.2 | 50.2 | $-2184.55 | -6.2% | $-1184.55 | -3.7 | done | losing for real |
| coinflip | 5021 | 49.9 | 50.0 | $-2308.58 | -4.6% | $-1308.58 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5021 | 50.3 | 51.4 | $-2959.42 | -5.9% | $-1959.42 | -4.3 | done | losing for real |
| always_up | 5021 | 47.9 | 49.3 | $-3645.83 | -7.3% | $-2645.83 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8468 | 47.9 | 48.8 | $-5045.46 |
| ETH | 9135 | 48.2 | 48.2 | $-4806.84 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
