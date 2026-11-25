# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1370 windows, 35662 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 708 | 34.2 | 35.4 | $-559.64 | -7.9% | $440.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1727 | 38.7 | 39.2 | $-808.68 | -4.7% | $191.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3564 | 50.9 | 50.1 | $-1003.45 | -2.8% | $-3.45 | -1.7 | done | can't tell from luck |
| value_ev5 | 2603 | 40.5 | 41.1 | $-1300.78 | -5.0% | $-300.78 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2990 | 49.3 | 49.4 | $-1495.42 | -5.0% | $-495.42 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2990 | 50.7 | 50.9 | $-1516.32 | -5.1% | $-516.32 | -2.8 | done | losing for real |
| trend_filter | 2120 | 48.5 | 50.4 | $-1873.46 | -8.8% | $-873.46 | -4.2 | done | losing for real |
| coinflip | 5132 | 50.0 | 50.0 | $-2200.35 | -4.3% | $-1200.35 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3564 | 49.1 | 50.2 | $-2217.40 | -6.2% | $-1217.40 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5132 | 50.1 | 51.3 | $-3209.84 | -6.3% | $-2209.84 | -4.6 | done | losing for real |
| always_up | 5132 | 47.9 | 49.3 | $-3703.34 | -7.2% | $-2703.34 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8835 | 47.9 | 48.8 | $-5159.67 |
| ETH | 9517 | 48.1 | 48.1 | $-5144.77 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
