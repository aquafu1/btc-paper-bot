# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1588 windows, 38553 settled trades, 409 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 811 | 34.4 | 35.1 | $-589.27 | -7.3% | $410.73 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3805 | 50.9 | 50.0 | $-968.10 | -2.5% | $31.90 | -1.6 | done | can't tell from luck |
| value_ev10 | 1918 | 38.5 | 39.0 | $-1003.95 | -5.2% | $-3.95 | -1.9 | done | can't tell from luck |
| value_ev5 | 2878 | 40.5 | 41.0 | $-1439.51 | -5.0% | $-439.51 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3186 | 51.0 | 50.9 | $-1497.76 | -4.7% | $-497.76 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3186 | 49.0 | 49.2 | $-1678.08 | -5.3% | $-678.08 | -3.0 | done | losing for real |
| trend_filter | 2266 | 48.5 | 50.3 | $-1984.92 | -8.8% | $-984.92 | -4.3 | done | losing for real |
| coinflip | 5566 | 50.1 | 49.9 | $-2304.14 | -4.1% | $-1304.14 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3805 | 49.1 | 50.2 | $-2373.14 | -6.2% | $-1373.14 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5566 | 50.1 | 51.3 | $-3458.53 | -6.2% | $-2458.53 | -4.8 | done | losing for real |
| always_up | 5566 | 48.2 | 49.1 | $-3559.70 | -6.4% | $-2559.70 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10214 | 48.0 | 48.6 | $-5707.69 |
| ETH | 11029 | 48.0 | 47.7 | $-5565.19 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
