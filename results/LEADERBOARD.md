# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 887 windows, 24481 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1123 | 38.3 | 39.1 | $-591.54 | -5.3% | $408.46 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2070 | 50.0 | 49.8 | $-910.72 | -4.4% | $89.28 | -2.0 | done | losing for real |
| trend_filter | 1443 | 50.1 | 51.0 | $-951.24 | -6.6% | $48.76 | -2.6 | done | losing for real |
| value_ev5 | 1698 | 39.9 | 41.0 | $-1018.51 | -6.0% | $-18.51 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2498 | 50.5 | 50.4 | $-1029.67 | -4.1% | $-29.67 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2498 | 49.5 | 50.4 | $-1371.37 | -5.5% | $-371.37 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2070 | 50.0 | 50.9 | $-1376.55 | -6.6% | $-376.55 | -3.1 | done | losing for real |
| coinflip | 3540 | 50.3 | 50.3 | $-1540.83 | -4.4% | $-540.83 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3540 | 51.3 | 51.7 | $-1586.80 | -4.5% | $-586.80 | -2.8 | done | losing for real |
| always_up | 3540 | 46.8 | 49.6 | $-3522.16 | -9.9% | $-2522.16 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5579 | 48.3 | 49.1 | $-3050.03 |
| ETH | 6095 | 48.2 | 48.5 | $-3791.30 |
| SOL | 6389 | 48.2 | 48.5 | $-3603.23 |
| XRP | 6418 | 48.4 | 48.5 | $-3554.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
