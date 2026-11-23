# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1179 windows, 32591 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 633 | 35.1 | 35.3 | $-329.65 | -5.2% | $670.35 | -1.0 | done | can't tell from luck |
| value_ev10 | 1543 | 38.6 | 39.2 | $-767.44 | -5.0% | $232.56 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3266 | 50.8 | 50.4 | $-1034.39 | -3.2% | $-34.39 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2747 | 49.6 | 49.4 | $-1216.81 | -4.4% | $-216.81 | -2.3 | done | losing for real |
| value_ev5 | 2336 | 40.3 | 41.1 | $-1256.14 | -5.4% | $-256.14 | -2.2 | done | losing for real |
| trend_filter | 1929 | 48.9 | 50.5 | $-1572.36 | -8.2% | $-572.36 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2747 | 50.4 | 51.1 | $-1682.32 | -6.1% | $-682.32 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3266 | 49.2 | 50.2 | $-1990.97 | -6.1% | $-990.97 | -3.5 | done | losing for real |
| coinflip | 4708 | 50.0 | 50.2 | $-2142.72 | -4.6% | $-1142.72 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4708 | 50.1 | 51.4 | $-2983.92 | -6.3% | $-1983.92 | -4.5 | done | losing for real |
| always_up | 4708 | 47.8 | 49.3 | $-3456.76 | -7.3% | $-2456.76 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7478 | 48.2 | 48.9 | $-4066.07 |
| ETH | 8083 | 48.1 | 48.4 | $-4826.54 |
| SOL | 8473 | 48.1 | 48.4 | $-4463.48 |
| XRP | 8557 | 48.1 | 48.2 | $-5077.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
