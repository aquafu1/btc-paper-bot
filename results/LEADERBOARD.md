# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1586 windows, 38534 settled trades, 382 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 810 | 34.4 | 35.1 | $-579.27 | -7.2% | $420.73 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3805 | 50.9 | 50.0 | $-968.10 | -2.5% | $31.90 | -1.6 | done | can't tell from luck |
| value_ev10 | 1915 | 38.5 | 39.0 | $-986.47 | -5.2% | $13.53 | -1.8 | done | can't tell from luck |
| value_ev5 | 2875 | 40.5 | 41.0 | $-1422.04 | -4.9% | $-422.04 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3186 | 51.0 | 50.9 | $-1497.76 | -4.7% | $-497.76 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3186 | 49.0 | 49.2 | $-1678.08 | -5.3% | $-678.08 | -3.0 | done | losing for real |
| trend_filter | 2266 | 48.5 | 50.3 | $-1984.92 | -8.8% | $-984.92 | -4.3 | done | losing for real |
| coinflip | 5562 | 50.1 | 49.9 | $-2275.75 | -4.1% | $-1275.75 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3805 | 49.1 | 50.2 | $-2373.14 | -6.2% | $-1373.14 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5562 | 50.2 | 51.3 | $-3430.14 | -6.2% | $-2430.14 | -4.7 | done | losing for real |
| always_up | 5562 | 48.2 | 49.1 | $-3519.70 | -6.3% | $-2519.70 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10206 | 48.0 | 48.6 | $-5652.74 |
| ETH | 11018 | 48.0 | 47.7 | $-5478.41 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
