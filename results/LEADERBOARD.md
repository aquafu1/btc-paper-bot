# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1425 windows, 36450 settled trades, 453 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 732 | 34.7 | 35.3 | $-485.63 | -6.6% | $514.37 | -1.4 | done | can't tell from luck |
| value_ev10 | 1768 | 38.9 | 39.2 | $-777.88 | -4.4% | $222.12 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3639 | 50.9 | 50.1 | $-1009.80 | -2.8% | $-9.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 2669 | 40.6 | 41.1 | $-1252.32 | -4.7% | $-252.32 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3060 | 49.2 | 49.3 | $-1508.56 | -4.9% | $-508.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3060 | 50.8 | 51.0 | $-1559.38 | -5.1% | $-559.38 | -2.9 | done | losing for real |
| trend_filter | 2163 | 48.5 | 50.3 | $-1893.07 | -8.8% | $-893.07 | -4.2 | done | losing for real |
| coinflip | 5240 | 50.1 | 50.0 | $-2217.15 | -4.2% | $-1217.15 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3639 | 49.1 | 50.2 | $-2247.09 | -6.2% | $-1247.09 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5240 | 50.2 | 51.3 | $-3254.00 | -6.2% | $-2254.00 | -4.6 | done | losing for real |
| always_up | 5240 | 47.9 | 49.3 | $-3651.88 | -7.0% | $-2651.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9224 | 48.1 | 48.8 | $-4961.99 |
| ETH | 9916 | 48.1 | 48.0 | $-5310.54 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
