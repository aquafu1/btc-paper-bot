# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 146 windows, 3670 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 252 | 60.7 | 53.1 | $+292.92 | +11.6% | $1292.92 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 353 | 56.4 | 52.2 | $+186.43 | +5.3% | $1186.43 | +1.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 576 | 52.8 | 51.4 | $-101.99 | -1.8% | $898.01 | -0.4 | done | can't tell from luck |
| value_ev20 | 73 | 31.5 | 37.1 | $-158.09 | -21.7% | $841.91 | -1.6 | Sun 12:45 AM | too few trades (73/200) |
| coinflip | 576 | 51.6 | 50.9 | $-210.07 | -3.6% | $789.93 | -0.9 | done | can't tell from luck |
| value_ev10 | 193 | 36.8 | 40.6 | $-277.90 | -14.4% | $722.10 | -1.7 | Thu 7:15 AM | too few trades (193/200) |
| trend_filter | 186 | 41.4 | 49.3 | $-360.99 | -19.4% | $639.01 | -2.7 | Thu 8:45 AM | too few trades (186/200) |
| value_ev5 | 280 | 37.9 | 42.2 | $-417.48 | -14.9% | $582.52 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 353 | 43.6 | 50.1 | $-568.66 | -16.1% | $431.34 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 252 | 39.3 | 49.2 | $-577.82 | -22.9% | $422.18 | -3.7 | done | losing for real |
| always_up | 576 | 46.2 | 49.9 | $-700.96 | -12.2% | $299.04 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 783 | 45.7 | 49.5 | $-838.25 |
| ETH | 906 | 45.4 | 48.8 | $-1025.61 |
| SOL | 968 | 48.3 | 48.8 | $-722.84 |
| XRP | 1013 | 50.5 | 49.1 | $-307.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
