# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 994 windows, 27654 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2821 | 51.0 | 50.4 | $-870.85 | -3.1% | $129.15 | -1.6 | done | can't tell from luck |
| value_ev10 | 1261 | 37.5 | 39.1 | $-898.79 | -7.1% | $101.21 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2379 | 49.8 | 49.7 | $-1116.46 | -4.7% | $-116.46 | -2.3 | done | losing for real |
| trend_filter | 1659 | 49.5 | 50.8 | $-1244.66 | -7.5% | $-244.66 | -3.1 | done | losing for real |
| value_ev5 | 1913 | 39.6 | 41.0 | $-1260.50 | -6.6% | $-260.50 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2379 | 50.2 | 50.9 | $-1535.71 | -6.5% | $-535.71 | -3.2 | done | losing for real |
| coinflip | 3972 | 50.3 | 50.3 | $-1732.68 | -4.4% | $-732.68 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2821 | 49.0 | 50.4 | $-1904.40 | -6.8% | $-904.40 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3972 | 50.7 | 51.5 | $-2183.26 | -5.5% | $-1183.26 | -3.6 | done | losing for real |
| always_up | 3972 | 46.9 | 49.6 | $-3913.57 | -9.9% | $-2913.57 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6304 | 48.2 | 49.1 | $-3509.06 |
| ETH | 6869 | 48.0 | 48.5 | $-4470.99 |
| SOL | 7228 | 48.1 | 48.6 | $-4291.79 |
| XRP | 7253 | 48.0 | 48.4 | $-4674.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
