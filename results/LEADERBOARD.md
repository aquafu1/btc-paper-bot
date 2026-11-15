# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 395 windows, 10819 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sat 11:15 PM | too few trades (199/200) |
| value_ev10 | 516 | 40.3 | 40.5 | $-185.67 | -3.6% | $814.33 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 917 | 50.6 | 49.8 | $-229.06 | -2.5% | $770.94 | -0.8 | done | can't tell from luck |
| value_ev5 | 763 | 41.9 | 42.1 | $-301.20 | -3.9% | $698.80 | -0.9 | done | can't tell from luck |
| trend_filter | 613 | 49.8 | 50.6 | $-342.33 | -5.6% | $657.67 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1089 | 49.1 | 49.8 | $-523.52 | -4.8% | $476.48 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1089 | 50.9 | 52.0 | $-660.37 | -6.1% | $339.63 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 917 | 49.4 | 52.1 | $-821.10 | -9.0% | $178.90 | -2.8 | done | losing for real |
| coinflip | 1572 | 49.9 | 50.8 | $-832.57 | -5.3% | $167.43 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1572 | 49.9 | 51.6 | $-1053.83 | -6.7% | $-53.83 | -2.8 | done | losing for real |
| always_up | 1572 | 46.5 | 50.7 | $-1851.92 | -11.8% | $-851.92 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2449 | 47.7 | 49.4 | $-1691.23 |
| ETH | 2715 | 48.0 | 48.9 | $-1649.71 |
| SOL | 2799 | 48.0 | 49.5 | $-2078.56 |
| XRP | 2856 | 48.9 | 49.2 | $-1439.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
