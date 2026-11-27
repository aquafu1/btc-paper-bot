# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1533 windows, 37843 settled trades, 378 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 771 | 34.5 | 35.3 | $-566.25 | -7.3% | $433.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3756 | 50.9 | 50.0 | $-958.99 | -2.6% | $41.01 | -1.6 | done | can't tell from luck |
| value_ev10 | 1854 | 38.6 | 39.2 | $-967.26 | -5.2% | $32.74 | -1.8 | done | can't tell from luck |
| value_ev5 | 2796 | 40.6 | 41.1 | $-1361.63 | -4.9% | $-361.63 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3151 | 51.1 | 51.0 | $-1454.01 | -4.6% | $-454.01 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3151 | 48.9 | 49.2 | $-1697.42 | -5.4% | $-697.42 | -3.0 | done | losing for real |
| trend_filter | 2240 | 48.6 | 50.3 | $-1923.62 | -8.6% | $-923.62 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3756 | 49.1 | 50.2 | $-2347.73 | -6.3% | $-1347.73 | -3.9 | done | losing for real |
| coinflip | 5456 | 49.9 | 50.0 | $-2414.95 | -4.4% | $-1414.95 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5456 | 50.1 | 51.3 | $-3392.77 | -6.2% | $-2392.77 | -4.7 | done | losing for real |
| always_up | 5456 | 48.1 | 49.2 | $-3590.64 | -6.6% | $-2590.64 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9885 | 47.9 | 48.7 | $-5602.47 |
| ETH | 10648 | 48.1 | 47.9 | $-5488.57 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
