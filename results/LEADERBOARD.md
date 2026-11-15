# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 400 windows, 10967 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 12:45 AM | too few trades (199/200) |
| value_ev10 | 518 | 40.5 | 40.5 | $-164.41 | -3.2% | $835.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 932 | 50.8 | 49.8 | $-200.09 | -2.1% | $799.91 | -0.7 | done | can't tell from luck |
| value_ev5 | 775 | 42.2 | 42.2 | $-267.60 | -3.5% | $732.40 | -0.8 | done | can't tell from luck |
| trend_filter | 622 | 50.0 | 50.6 | $-314.40 | -5.1% | $685.60 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1102 | 49.5 | 49.8 | $-449.98 | -4.1% | $550.02 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1102 | 50.5 | 52.1 | $-733.79 | -6.7% | $266.21 | -2.3 | done | losing for real |
| coinflip | 1595 | 50.1 | 50.9 | $-790.53 | -5.0% | $209.47 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 932 | 49.2 | 52.1 | $-854.41 | -9.2% | $145.59 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1595 | 49.8 | 51.6 | $-1073.03 | -6.7% | $-73.03 | -2.8 | done | losing for real |
| always_up | 1595 | 46.0 | 50.8 | $-2027.06 | -12.7% | $-1027.06 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2473 | 47.8 | 49.5 | $-1698.13 |
| ETH | 2757 | 48.0 | 49.0 | $-1670.93 |
| SOL | 2838 | 48.0 | 49.5 | $-2115.67 |
| XRP | 2899 | 48.9 | 49.3 | $-1447.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
