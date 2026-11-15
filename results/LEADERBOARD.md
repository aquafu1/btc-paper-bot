# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 441 windows, 12144 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1038 | 51.3 | 50.0 | $-179.94 | -1.7% | $820.06 | -0.6 | done | can't tell from luck |
| value_ev20 | 222 | 34.2 | 36.1 | $-198.23 | -8.9% | $801.77 | -1.0 | done | can't tell from luck |
| trend_filter | 701 | 50.4 | 50.6 | $-329.69 | -4.7% | $670.31 | -1.3 | done | can't tell from luck |
| value_ev10 | 573 | 38.4 | 40.2 | $-463.63 | -8.1% | $536.37 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1225 | 49.6 | 50.0 | $-557.63 | -4.6% | $442.37 | -1.6 | done | can't tell from luck |
| value_ev5 | 851 | 40.8 | 41.9 | $-559.11 | -6.6% | $440.89 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1225 | 50.4 | 51.7 | $-834.70 | -6.8% | $165.30 | -2.5 | done | losing for real |
| coinflip | 1757 | 50.4 | 50.9 | $-845.43 | -4.8% | $154.57 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1038 | 48.7 | 51.8 | $-1055.00 | -10.2% | $-55.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1757 | 49.7 | 51.5 | $-1265.03 | -7.2% | $-265.03 | -3.1 | done | losing for real |
| always_up | 1757 | 45.9 | 50.5 | $-2248.84 | -12.8% | $-1248.84 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2745 | 47.5 | 49.3 | $-2142.98 |
| ETH | 3047 | 47.9 | 48.8 | $-1969.73 |
| SOL | 3157 | 47.7 | 49.3 | $-2570.36 |
| XRP | 3195 | 48.6 | 49.3 | $-1854.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
