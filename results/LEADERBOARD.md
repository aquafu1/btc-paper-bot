# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1659 windows, 39484 settled trades, 372 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 842 | 34.3 | 35.2 | $-641.08 | -7.6% | $358.92 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3878 | 50.8 | 49.9 | $-1022.36 | -2.6% | $-22.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1990 | 38.2 | 39.0 | $-1172.06 | -5.9% | $-172.06 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3242 | 51.1 | 50.9 | $-1436.36 | -4.4% | $-436.36 | -2.6 | done | losing for real |
| value_ev5 | 2972 | 40.2 | 41.0 | $-1684.76 | -5.7% | $-684.76 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3242 | 48.9 | 49.2 | $-1822.51 | -5.6% | $-822.51 | -3.2 | done | losing for real |
| trend_filter | 2310 | 48.3 | 50.4 | $-2134.47 | -9.2% | $-1134.47 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3878 | 49.2 | 50.2 | $-2364.79 | -6.1% | $-1364.79 | -3.8 | done | losing for real |
| coinflip | 5710 | 49.9 | 49.9 | $-2500.23 | -4.4% | $-1500.23 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5710 | 50.2 | 51.3 | $-3509.30 | -6.1% | $-2509.30 | -4.8 | done | losing for real |
| always_up | 5710 | 48.3 | 49.0 | $-3542.66 | -6.2% | $-2542.66 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10642 | 47.9 | 48.5 | $-6100.11 |
| ETH | 11532 | 47.9 | 47.6 | $-6146.23 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
