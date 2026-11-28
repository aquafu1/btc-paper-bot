# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1653 windows, 39417 settled trades, 372 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 840 | 34.4 | 35.2 | $-621.08 | -7.4% | $378.92 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3873 | 50.8 | 49.9 | $-1031.30 | -2.7% | $-31.30 | -1.6 | done | can't tell from luck |
| value_ev10 | 1983 | 38.3 | 39.0 | $-1127.41 | -5.7% | $-127.41 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3242 | 51.1 | 50.9 | $-1436.36 | -4.4% | $-436.36 | -2.6 | done | losing for real |
| value_ev5 | 2961 | 40.3 | 41.0 | $-1600.10 | -5.4% | $-600.10 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3242 | 48.9 | 49.2 | $-1822.51 | -5.6% | $-822.51 | -3.2 | done | losing for real |
| trend_filter | 2309 | 48.3 | 50.4 | $-2124.47 | -9.2% | $-1124.47 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3873 | 49.2 | 50.2 | $-2348.00 | -6.1% | $-1348.00 | -3.8 | done | losing for real |
| coinflip | 5698 | 49.9 | 49.9 | $-2512.26 | -4.4% | $-1512.26 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5698 | 50.2 | 51.3 | $-3544.72 | -6.2% | $-2544.72 | -4.8 | done | losing for real |
| always_up | 5698 | 48.2 | 49.0 | $-3544.79 | -6.2% | $-2544.79 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10610 | 47.9 | 48.5 | $-5980.10 |
| ETH | 11497 | 47.9 | 47.6 | $-6148.66 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
