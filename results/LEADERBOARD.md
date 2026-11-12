# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 175 windows, 4488 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 437 | 58.1 | 52.3 | $+348.87 | +8.0% | $1348.87 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 331 | 59.8 | 53.2 | $+320.88 | +9.7% | $1320.88 | +1.9 | done | can't tell from luck |
| value_ev20 | 86 | 33.7 | 36.7 | $-133.13 | -15.5% | $866.87 | -1.2 | Sun 2:15 AM | too few trades (86/200) |
| value_ev10 | 226 | 37.2 | 40.5 | $-302.61 | -13.4% | $697.39 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 693 | 51.1 | 51.2 | $-303.68 | -4.4% | $696.32 | -1.2 | done | can't tell from luck |
| coinflip | 693 | 49.9 | 50.9 | $-438.00 | -6.3% | $562.00 | -1.7 | done | can't tell from luck |
| trend_filter | 228 | 40.8 | 49.2 | $-447.69 | -19.6% | $552.31 | -3.0 | done | losing for real |
| value_ev5 | 333 | 38.4 | 42.4 | $-453.99 | -13.6% | $546.01 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 331 | 40.2 | 48.8 | $-694.48 | -21.0% | $305.52 | -3.8 | done | losing for real |
| always_up | 693 | 46.5 | 49.9 | $-793.53 | -11.5% | $206.47 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 437 | 41.9 | 49.7 | $-828.35 | -19.0% | $171.65 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 973 | 45.8 | 49.3 | $-967.60 |
| ETH | 1122 | 45.6 | 48.8 | $-1318.17 |
| SOL | 1173 | 47.6 | 48.9 | $-1042.94 |
| XRP | 1220 | 49.8 | 49.0 | $-397.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
