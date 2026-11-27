# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 1:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1558 windows, 38210 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 792 | 34.3 | 35.3 | $-590.62 | -7.5% | $409.38 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3784 | 50.9 | 50.0 | $-992.20 | -2.6% | $7.80 | -1.6 | done | can't tell from luck |
| value_ev10 | 1885 | 38.4 | 39.1 | $-1016.42 | -5.4% | $-16.42 | -1.9 | done | can't tell from luck |
| value_ev5 | 2832 | 40.4 | 41.0 | $-1440.07 | -5.1% | $-440.07 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3179 | 51.0 | 50.9 | $-1511.86 | -4.8% | $-511.86 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3179 | 49.0 | 49.2 | $-1665.05 | -5.2% | $-665.05 | -2.9 | done | losing for real |
| trend_filter | 2257 | 48.6 | 50.3 | $-1931.52 | -8.6% | $-931.52 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3784 | 49.1 | 50.2 | $-2334.05 | -6.2% | $-1334.05 | -3.8 | done | losing for real |
| coinflip | 5506 | 50.0 | 49.9 | $-2367.67 | -4.3% | $-1367.67 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5506 | 50.2 | 51.3 | $-3426.12 | -6.2% | $-2426.12 | -4.8 | done | losing for real |
| always_up | 5506 | 48.2 | 49.2 | $-3519.15 | -6.4% | $-2519.15 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10057 | 47.9 | 48.6 | $-5735.69 |
| ETH | 10843 | 48.1 | 47.8 | $-5474.81 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
