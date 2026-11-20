# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 905 windows, 24987 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1143 | 38.4 | 39.1 | $-563.08 | -4.9% | $436.92 | -1.3 | done | can't tell from luck |
| value_ev5 | 1730 | 40.1 | 41.0 | $-947.46 | -5.5% | $52.54 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2113 | 49.9 | 49.8 | $-957.71 | -4.5% | $42.29 | -2.1 | done | losing for real |
| trend_filter | 1481 | 49.9 | 51.0 | $-1018.98 | -6.9% | $-18.98 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2549 | 50.4 | 50.5 | $-1068.40 | -4.2% | $-68.40 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2549 | 49.6 | 50.4 | $-1327.49 | -5.2% | $-327.49 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2113 | 50.1 | 50.9 | $-1339.95 | -6.3% | $-339.95 | -3.0 | done | losing for real |
| coinflip | 3615 | 50.2 | 50.3 | $-1595.95 | -4.4% | $-595.95 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3615 | 51.2 | 51.7 | $-1664.16 | -4.6% | $-664.16 | -2.9 | done | losing for real |
| always_up | 3615 | 46.8 | 49.7 | $-3580.97 | -9.9% | $-2580.97 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5690 | 48.3 | 49.1 | $-3105.74 |
| ETH | 6213 | 48.2 | 48.5 | $-3718.73 |
| SOL | 6522 | 48.2 | 48.6 | $-3704.85 |
| XRP | 6562 | 48.3 | 48.5 | $-3636.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
